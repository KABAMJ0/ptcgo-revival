from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6aba520f-473e-51a9-a82c-01f54107203c",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mightyena.Name",
    display_name="Mightyena",
    searchable_by=["Mightyena", "Stage 1", "Mightyena"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poochyena.Name",
    family_id=261,
    abilities=[
        Ability(
            title="Cold Feet",
            game_text="If Mightyena is affected by a Special Condition, ignore all Energy necessary to use Mightyena's attacks.",
            effect=unimplemented,
        ),
        Attack(
            title="Collude",
            game_text="If you played any Supporter card from your hand during this turn, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Desperate Attack",
            game_text="If Mightyena has less Energy attached to it than the Defending Pok\u00e9mon, this attack does 50 damage plus 30 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)