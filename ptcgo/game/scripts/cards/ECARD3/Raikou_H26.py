from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _is_lightning(card) -> bool:
    return energy_provides_type(card, PokemonTypes.LIGHTNING.value)


async def _lightning_sphere(ctx):
    await ctx.deal_damage()
    heads = await ctx.flip_coins(1, "Lightning Sphere")
    if not (heads and heads[0]):
        return
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 99, predicate=_is_lightning,
        prompt="Choose Lightning Energy to discard from Raikou")
    if discarded:
        await ctx.deal_damage(20 * len(discarded))

card = PokemonCardDef(
    guid="8a27c009-45e6-535f-9ebb-9b1a8b12db9a",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raikou.Name",
    display_name="Raikou",
    searchable_by=["Raikou", "Basic", "Raikou"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="ECARD3",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=243,
    abilities=[
        Ability(
            title="Pure Body",
            game_text="To attach a Lightning Energy card from your hand to Raikou, you must discard an Energy card attached to Raikou. (Attach the Lightning Energy, and then discard an Energy card from Raikou.)",
            effect=unimplemented,
        ),
        Attack(
            title="Lightning Sphere",
            game_text="You may flip a coin. If heads, discard all Lightning Energy cards attached to Raikou. This attack does 40 damage plus 20 more damage for each Energy card discarded in this way.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=_lightning_sphere,
        ),
    ],
)
