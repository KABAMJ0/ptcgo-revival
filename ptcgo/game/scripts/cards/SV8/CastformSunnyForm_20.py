from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="4a4ea754-bbc8-5c24-aadb-c5169d97c583",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CastformSunnyForm.Name",
    display_name="Castform Sunny Form",
    searchable_by=["Castform Sunny Form", "Basic", "CastformSunnyForm"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    family_id=351,
    abilities=[
        Attack(
            title="Singe",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Sunny Assist",
            game_text="Move all Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)