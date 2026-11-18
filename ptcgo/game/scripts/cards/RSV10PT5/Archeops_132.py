from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8ae15689-d610-52d5-a52b-81e6ef17410c",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archeops.Name",
    display_name="Archeops",
    searchable_by=["Archeops", "Stage 2", "Archeops"],
    subtypes=["Stage 2"],
    collector_number=132,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Archen.Name",
    family_id=566,
    abilities=[
        Ability(
            title="Ancient Wing",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may devolve 1 of your opponent's evolved Pok\u00e9mon by putting the highest Stage Evolution card on it into your opponent's hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)