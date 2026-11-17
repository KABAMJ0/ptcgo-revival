from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7a38ed11-0450-53b4-9db6-90be9cc15a5b",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WormadamPlantCloak.Name",
    display_name="Wormadam Plant Cloak",
    searchable_by=["Wormadam Plant Cloak", "Stage 1", "WormadamPlantCloak"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BurmyPlantCloak.Name",
    family_id=412,
    abilities=[
        Attack(
            title="Magical Needle",
            game_text="Remove 2 damage counters from 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Cloak Scale",
            game_text="If you have Wormadam Sandy Cloak in play, the Defending Pok\u00e9mon is now Burned, Confused, and Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)