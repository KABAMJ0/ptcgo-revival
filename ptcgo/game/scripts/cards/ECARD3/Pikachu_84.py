from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _is_lightning(card) -> bool:
    return energy_provides_type(card, PokemonTypes.LIGHTNING.value)


async def _max_voltage(ctx):
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 99, predicate=_is_lightning,
        prompt="Choose Lightning Energy to discard from Pikachu")
    await ctx.deal_damage(20 + 10 * len(discarded))

card = PokemonCardDef(
    guid="3f2853b5-288a-5214-8426-950666daaf40",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Max Voltage",
            game_text="Discard all Lightning Energy cards attached to Pikachu. This attack does 20 damage plus 10 more damage for each Energy card discarded in this way.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=_max_voltage,
        ),
    ],
)
