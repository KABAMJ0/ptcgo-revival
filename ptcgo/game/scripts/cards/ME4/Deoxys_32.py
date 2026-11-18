from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="84d50dd2-04ad-5997-b22a-78db33a73af2",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys",
    searchable_by=["Deoxys", "Basic", "Deoxys"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="ME4",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=386,
    abilities=[
        Attack(
            title="Psyspear",
            game_text="If this Pok\u00e9mon has at least 2 extra Energy attached (in addition to this attack's cost), this attack also does 120 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=120,
            effect=unimplemented,
        ),
    ],
)