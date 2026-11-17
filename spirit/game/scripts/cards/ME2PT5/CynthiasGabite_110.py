from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7e84a958-02d5-5ec9-a641-c825b8e61e64",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGabite.Name",
    display_name="Cynthia's Gabite",
    searchable_by=["Cynthia's Gabite", "Stage 1", "CynthiasGabite"],
    subtypes=["Stage 1"],
    collector_number=110,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGible.Name",
    family_id=443,
    abilities=[
        Ability(
            title="Champion's Call",
            game_text="Once during your turn, you may search your deck for a Cynthia's Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Dragonslice",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
    ],
)