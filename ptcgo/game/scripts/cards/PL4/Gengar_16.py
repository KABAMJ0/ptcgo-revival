from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.passives_common import move_counters_ability


_move_counters, _can_move = move_counters_ability(1, "theirs")


def _curse_ready(board, player_id, pokemon) -> bool:
    return _can_move(board, player_id, pokemon) and \
        not pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS)

card = PokemonCardDef(
    guid="0d16fcb9-b210-5456-bb90-07138dd64598",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2", "Gengar"],
    subtypes=["Stage 2"],
    collector_number=16,
    set_code="PL4",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Curse",
            game_text="Once during your turn (before your attack), you may move 1 damage counter from 1 of your opponent's Pok\u00e9mon to another of your opponent's Pok\u00e9mon. This power can't be used if Gengar is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_curse_ready,
            effect=_move_counters,
        ),
        Attack(
            title="Shadow Skip",
            game_text="Does 10 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) You may switch Gengar with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
    ],
)