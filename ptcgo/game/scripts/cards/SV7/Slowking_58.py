from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="204edd67-b561-5e10-a1e7-3102b0a9d477",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowking.Name",
    display_name="Slowking",
    searchable_by=["Slowking", "Stage 1", "Slowking"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="SV7",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Attack(
            title="Seek Inspiration",
            game_text="Discard the top card of your deck, and if that card is a Pok\u00e9mon that doesn't have a Rule Box, choose 1 of its attacks and use it as this attack. (Pok\u00e9mon ex, Pok\u00e9mon V, etc. have Rule Boxes.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)