from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

async def mist_ball(ctx):
    """Printed 110; on tails discard a Fire Energy and a Psychic Energy."""
    from ptcgo.game.card_effects.pokemon import energy_provides_type
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Mist Ball")
    if results and results[0]:
        return
    for type_value, label in ((PokemonTypes.FIRE.value, "Fire"),
                              (PokemonTypes.PSYCHIC.value, "Psychic")):
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            predicate=lambda c, t=type_value: energy_provides_type(c, t),
            prompt=f"Choose a {label} Energy to discard")


card = PokemonCardDef(
    guid="7e5e3f48-9d75-5cc7-837a-e7197185ffb6",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias",
    searchable_by=["Latias", "Basic", "Latias"],
    subtypes=["Basic"],
    collector_number=135,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=380,
    abilities=[
        Attack(
            title="Hypnoblast",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Mist Ball",
            game_text="Flip a coin. If tails, discard a Fire Energy and a Psychic Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=mist_ball,
        ),
    ],
)