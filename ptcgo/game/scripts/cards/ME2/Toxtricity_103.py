from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e7d75e55-1863-5e02-ae17-85548d2a4013",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricity.Name",
    display_name="Toxtricity",
    searchable_by=["Toxtricity", "Stage 1", "Toxtricity"],
    subtypes=["Stage 1"],
    collector_number=103,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    family_id=848,
    abilities=[
        Ability(
            title="Sinister Surge",
            game_text="Once during your turn, you may use this Ability. Search your deck for a Basic Darkness Energy card and attach it to 1 of your Benched Darkness Pok\u00e9mon. Then, shuffle your deck. If you attached Energy to a Pok\u00e9mon in this way, place 2 damage counters on that Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)