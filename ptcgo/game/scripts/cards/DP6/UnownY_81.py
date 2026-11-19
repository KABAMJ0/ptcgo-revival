from ptcgo.game.data_utils import def_for
from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.session.effects import is_trainer_card
from ptcgo.game.card_effects.passives_common import Passive, is_in_active_spot
from ptcgo.game.attributes import SpecialConditions, AttrID
from ptcgo.game.session.effects import full_stack
from ptcgo.game.session.passives import carrier_pokemon
from ptcgo.game.data_utils import Activations


async def _yawn(ctx):
    """YAWN: 1 counter off an Active Unown and that Unown falls Asleep."""
    candidates = [p for p in ctx.my_pokemon_in_play()
                  if is_in_active_spot(p) and _display_name(p).startswith("Unown")
                  and p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not candidates:
        return
    target = await ctx.choose_pokemon(candidates, "Choose an Active Unown")
    if target is None:
        return
    await ctx.heal(10, target=target)
    await ctx.apply_special_condition(target, SpecialConditions.ASLEEP)


def _display_name(entity) -> str:
    """The printed name of a card on the board (empty when unknown)."""
    return getattr(def_for(getattr(entity, "archetype_id", "") or ""),
                   "display_name", "") or ""

card = PokemonCardDef(
    guid="cc6a7f11-9bf5-5914-a512-65bb7968b6c8",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownY.Name",
    display_name="Unown [Y]",
    searchable_by=["Unown [Y]", "Basic", "UnownY"],
    subtypes=["Basic"],
    collector_number=81,
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
            title="YAWN",
            game_text="Once during your turn (before your attack), if Unown Y is on your Bench, you may remove 1 damage counter from 1 of your Active Unown and that Unown is now Asleep.",
            activation=Activations.ONCE_PER_TURN,
            effect=_yawn,
        ),
        Attack(
            title="Hidden Power",
            game_text="Search your deck for up to 2 Trainer cards, show them to your opponent, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=search_to_hand(is_trainer_card, count=2, reveal=True),
        ),
    ],
)