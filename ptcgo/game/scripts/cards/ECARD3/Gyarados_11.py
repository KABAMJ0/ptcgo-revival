from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _flame_vapor(ctx):
    results = await ctx.flip_coins(2, "Flame Vapor")
    heads = sum(1 for result in results if result)
    defender = ctx.defender
    if not heads or defender is None:
        return
    for _ in range(heads):
        if not ctx.attached_energies(defender):
            break
        await ctx.discard_energy_from(
            defender, 1, prompt="Discard an Energy card attached to the Defending Pokémon")


card = PokemonCardDef(
    guid="99c2c542-a6f1-5396-a3d0-25d46f8e6d9e",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name",
    display_name="Gyarados",
    searchable_by=["Gyarados", "Stage 1", "Gyarados"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="ECARD3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        Ability(
            title="Flame Vapor",
            game_text="When you play Gyarados from your hand to evolve your Active Pok\u00e9mon, you may flip 2 coins. For each heads, discard an Energy card attached to the Defending Pok\u00e9mon.",
            trigger=Triggers.ON_EVOLVE,
            effect=_flame_vapor,
        ),
        Attack(
            title="Dragon's Vengeance",
            game_text="If Gyarados has 7 or more damage counters on it, this attack's base damage is 100.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=unimplemented,
        ),
    ],
)