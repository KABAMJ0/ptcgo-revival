from ptcgo.game.session.passives import carrier_pokemon
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import Passive, is_in_active_spot
from ptcgo.game.data_utils import def_for


class _Unseen(Passive):
    """Benched Unown are shielded from opposing attacks, damage and effects."""

    def _covers(self, target, carrier):
        return (target is not None
                and _display_name(target).startswith("Unown")
                and target is not None
                and not is_in_active_spot(target)
                and target.owning_player_id == carrier.owning_player_id
                and not is_in_active_spot(carrier_pokemon(carrier)))

    def prevents_damage(self, calc, carrier):
        return bool(calc.is_attack and calc.is_opposing
                    and self._covers(calc.target, carrier))

    def blocks_attack_effects(self, target, carrier, attacker=None, board=None):
        return self._covers(target, carrier)


async def _hidden_power_mill(ctx):
    """Hidden Power (Unown U): any 1 card out of the deck, discarded."""
    picked = await ctx.search_deck(count=1, minimum=1,
                                   prompt="Search your deck for any 1 card")
    if picked:
        await ctx.discard_cards(picked)
    await ctx.shuffle_deck()


def _display_name(entity) -> str:
    """The printed name of a card on the board (empty when unknown)."""
    return getattr(def_for(getattr(entity, "archetype_id", "") or ""),
                   "display_name", "") or ""

card = PokemonCardDef(
    guid="a6d593c7-9719-5a79-b6b4-dffb2252725b",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownU.Name",
    display_name="Unown [U]",
    searchable_by=["Unown [U]", "Basic", "UnownU"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="UNSEEN",
            game_text="As long as Unown U is on your Bench, prevent all effects of attacks, including damage, done by your opponent's Pok\u00e9mon to any Unown on your Bench.",
            passive=_Unseen(),
        ),
        Attack(
            title="Hidden Power",
            game_text="Search your deck for any 1 card and discard it. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_hidden_power_mill,
        ),
    ],
)