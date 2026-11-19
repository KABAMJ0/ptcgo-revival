from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import (
    attach_from_hand, hand_attach_condition,
)
from ptcgo.game.card_effects.trainers import basic_energy_of, pokemon_of

_STONE_ARMS_ENERGY = basic_energy_of("fighting")
_FIGHTING_POKEMON = pokemon_of("fighting")


card = PokemonCardDef(
    guid="39b00f40-f6d6-5fe1-a4db-bcf965a5bebb",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Barbaracle.Name",
    display_name="Barbaracle",
    searchable_by=["Barbaracle", "Stage 1", "Barbaracle"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Binacle.Name",
    family_id=688,
    abilities=[
        Ability(
            title="Stone Arms",
            game_text="Once during your turn, you may use this Ability. Attach a Basic Fighting Energy card from your hand to 1 of your Fighting Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            effect=attach_from_hand(_STONE_ARMS_ENERGY, count=1,
                                    target="choice", target_pred=_FIGHTING_POKEMON),
            condition=hand_attach_condition(_STONE_ARMS_ENERGY, target="choice",
                                           target_pred=_FIGHTING_POKEMON),
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)