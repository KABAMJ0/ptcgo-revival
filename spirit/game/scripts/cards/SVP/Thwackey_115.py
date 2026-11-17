from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="230f7959-996d-5590-8a0c-42c33a28eee7",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thwackey.Name",
    display_name="Thwackey",
    searchable_by=["Thwackey", "Stage 1", "Thwackey"],
    subtypes=["Stage 1"],
    collector_number=115,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grookey.Name",
    family_id=811,
    abilities=[
        Ability(
            title="Boom Boom Groove",
            game_text="Once during your turn, if your Active Pok\u00e9mon has the Festival Lead Ability, you may search your deck for a card and put it into your hand. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Beat",
            cost={PokemonTypes.GRASS: 2},
            damage=50,
        ),
    ],
)