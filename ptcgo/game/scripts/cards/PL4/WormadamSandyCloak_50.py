from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="13e40c49-d6f1-5d15-9f6d-bb2e2e998e50",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WormadamSandyCloak.Name",
    display_name="Wormadam Sandy Cloak",
    searchable_by=["Wormadam Sandy Cloak", "Stage 1", "WormadamSandyCloak"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BurmySandyCloak.Name",
    family_id=412,
    abilities=[
        Attack(
            title="Hang Down",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
        Attack(
            title="Cloak Headbutt",
            game_text="If you have Wormadam Trash Cloak in play, this attack does 60 damage plus 30 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)