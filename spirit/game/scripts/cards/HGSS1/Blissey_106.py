from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ca3c85e6-4140-5670-ab3b-8544ba46201b",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blissey.Name",
    display_name="Blissey",
    searchable_by=["Blissey", "Stage 1", "Prime", "Blissey"],
    subtypes=["Stage 1", "Prime"],
    collector_number=106,
    set_code="HGSS1",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    family_id=113,
    abilities=[
        Ability(
            title="Blissful Nurse",
            game_text="Once during your turn, when you play Blissey from your hand to evolve 1 of your Pok\u00e9mon, you may remove all damage counters from all of your Pok\u00e9mon. If you do, discard all Energy attached to those Pok\u00e9mon that had any damage counters on them.",
            effect=unimplemented,
        ),
        Attack(
            title="Strength",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)