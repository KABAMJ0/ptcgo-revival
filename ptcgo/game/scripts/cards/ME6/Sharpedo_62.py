from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_discard_opponent_energy

card = PokemonCardDef(
    guid="83c1270d-9b50-5ef0-80e8-af5371c57221",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sharpedo.Name",
    display_name="Sharpedo",
    searchable_by=["Sharpedo", "Stage 1", "Sharpedo"],
    subtypes=["Stage 1"],
    collector_number=62,
    set_code="ME6",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name",
    family_id=318,
    abilities=[
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=flip_discard_opponent_energy(),
        ),
    ],
)