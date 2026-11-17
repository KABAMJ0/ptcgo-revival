from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="194c38c6-2563-52c9-8cb9-1bca8c0c9d55",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palafin.Name",
    display_name="Palafin",
    searchable_by=["Palafin", "Stage 1", "Palafin"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name",
    family_id=963,
    abilities=[
        Ability(
            title="Zero to Hero",
            game_text="Once during your turn, when this Pok\u00e9mon moves from the Active Spot to the Bench, you may search your deck for a Palafin ex and switch it with this Pok\u00e9mon. Any attached cards, damage counters, Special Conditions, turns in play, and any other effects remain on the new Pok\u00e9mon. If you switched a Pok\u00e9mon in this way, put this card into your deck. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)