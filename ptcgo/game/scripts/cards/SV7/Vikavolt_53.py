from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3dd43ca4-0404-544e-b324-4c2e07bb2dde",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vikavolt.Name",
    display_name="Vikavolt",
    searchable_by=["Vikavolt", "Stage 2", "Vikavolt"],
    subtypes=["Stage 2"],
    collector_number=53,
    set_code="SV7",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name",
    family_id=736,
    abilities=[
        Attack(
            title="Volt Switch",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Lightning Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=90,
            effect=unimplemented,
        ),
        Attack(
            title="Sparking Strike",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=240,
        ),
    ],
)