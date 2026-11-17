from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="79244baa-602a-5d9a-91d3-66320c319290",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name",
    display_name="Slakoth",
    searchable_by=["Slakoth", "Basic", "Slakoth"],
    subtypes=["Basic"],
    collector_number=95,
    set_code="PL1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=287,
    abilities=[
        Attack(
            title="Flail",
            game_text="Does 10 damage times the number of damage counters on Slakoth.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Slack Off",
            game_text="Remove all damage counters from Slakoth. Slakoth can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)