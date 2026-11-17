from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9d4fcc3d-d6b0-544d-847b-777dcf17c591",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clawitzer.Name",
    display_name="Clawitzer",
    searchable_by=["Clawitzer", "Stage 1", "Clawitzer"],
    subtypes=["Stage 1"],
    collector_number=141,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clauncher.Name",
    family_id=692,
    abilities=[
        Ability(
            title="Fall Back to Reload",
            game_text="Once during your turn, when this Pok\u00e9mon moves from the Active Spot to your Bench, you may use this Ability. Attach up to 2 Basic Water Energy cards from your hand to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Aqua Launcher",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 3},
            damage=210,
            effect=unimplemented,
        ),
    ],
)