from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4cc0e913-bfa7-51d8-82c9-f2404170f3d8",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vikavolt.Name",
    display_name="Vikavolt",
    searchable_by=["Vikavolt", "Stage 2", "Vikavolt"],
    subtypes=["Stage 2"],
    collector_number=56,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name",
    family_id=736,
    abilities=[
        Attack(
            title="Mach Bolt",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=50,
        ),
        Attack(
            title="Circuit Cannon",
            game_text="This attack does 80 more damage for each of your Benched Charjabug.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)