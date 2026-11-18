from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0dc7af0a-687e-5388-8e9c-6cbf8112c5fc",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pachirisu.Name",
    display_name="Pachirisu",
    searchable_by=["Pachirisu", "Basic", "Pachirisu"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=417,
    abilities=[
        Ability(
            title="Electricity Pouches",
            game_text="This Pok\u00e9mon can't be Paralyzed.",
            effect=unimplemented,
        ),
        Attack(
            title="Everyone Discharge",
            game_text="This attack does 20 more damage for each of your Benched Lightning Pok\u00e9mon. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)