from ptcgo.game.card_effects.attacks_common import flip_defender_lock_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import basic_energy_of

card = PokemonCardDef(
    guid="682049b0-9fba-5abb-ba0e-156421c63cc3",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sealeo.Name",
    display_name="Sealeo",
    searchable_by=["Sealeo", "Stage 1", "Sealeo"],
    subtypes=["Stage 1"],
    collector_number=77,
    set_code="PL2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spheal.Name",
    family_id=363,
    abilities=[
        Attack(
            title="Find Ice",
            game_text="Search your deck for up to 2 Water Energy cards, show them to your opponent, and put them into your hand. Shuffle your deck afterward.",
            cost={},
            effect=search_to_hand(basic_energy_of("water"), count=2, reveal=True),
        ),
        Attack(
            title="Sheer Cold",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=flip_defender_lock_attack(),
        ),
    ],
)