from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import Passive, carrier_pokemon
from ptcgo.game.card_effects.support_common import entity_name


class _XXXXX(Passive):
    """Every Hidden Power from one of your Unown does 10 more per heads."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return None
        attacker = calc.attacker
        if attacker is None or attacker.owning_player_id != carrier.owning_player_id:
            return None
        if (calc.attack_title or "") != "Hidden Power":
            return None
        if "Unown" not in entity_name(attacker):
            return None
        if "XXXXX" in calc.applied_once:
            return None
        calc.applied_once.add("XXXXX")
        heads = await ctx.flip_until_tails("XXXXX")
        return calc.amount + 10 * heads


card = PokemonCardDef(
    guid="418e56ed-8520-53b3-8bb7-041cd1decb2b",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownX.Name",
    display_name="Unown [X]",
    searchable_by=["Unown [X]", "Basic", "UnownX"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[XXXXX]",
            game_text="Whenever 1 of your Pok\u00e9mon with Unown in its name uses its Hidden Power attack, flip a coin until you get tails. That attack does 10 more damage for each heads. If you have more than 1 Unown [X] in play, use only 1 [XXXXX] each turn.",
            passive=_XXXXX(),
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)