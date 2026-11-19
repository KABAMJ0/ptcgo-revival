from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of, is_basic_energy_card

card = PokemonCardDef(
    guid="1198ec4f-cfc0-5918-967c-3f21c4c9166a",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    display_name="Zweilous",
    searchable_by=["Zweilous", "Stage 1", "Zweilous"],
    subtypes=["Stage 1"],
    collector_number=96,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Deino.Name",
    family_id=633,
    abilities=[
        Attack(
            title="Draw In",
            game_text="Attach 2 Darkness Energy cards from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_discard(basic_energy_of("darkness"), count=2, minimum=0, target="self"),
        ),
        Attack(
            title="Dragon Headbutt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)