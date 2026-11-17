from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="75bfceba-3916-572f-835c-e58bfeab5f68",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miraidonex.Name",
    display_name="Miraidon ex",
    searchable_by=["Miraidon ex", "Basic", "ex", "Miraidonex"],
    subtypes=["Basic", "ex"],
    collector_number=253,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1008,
    abilities=[
        Ability(
            title="Tandem Unit",
            game_text="Once during your turn, you may search your deck for up to 2 Basic Lightning Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Photon Blaster",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=unimplemented,
        ),
    ],
)