from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="484f9f61-275c-5f0e-b0e9-4b25f6f3198a",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name",
    display_name="Gyarados",
    searchable_by=["Gyarados", "Stage 1", "Gyarados"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="ECARD3",
    rarity=Rarities.RareHolo,
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
            effect=unimplemented,
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