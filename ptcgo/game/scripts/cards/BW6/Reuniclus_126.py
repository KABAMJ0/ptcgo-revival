from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import move_counters_ability


_move_counters, _can_move = move_counters_ability(1, "mine")

card = PokemonCardDef(
    guid="c4952cce-7e7f-56c0-8d64-2cd4e7e31727",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reuniclus.Name",
    display_name="Reuniclus",
    searchable_by=["Reuniclus", "Stage 2", "Reuniclus"],
    subtypes=["Stage 2"],
    collector_number=126,
    set_code="BW6",
    rarity=Rarities.RareSecret,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duosion.Name",
    family_id=579,
    abilities=[
        Ability(
            title="Damage Swap",
            game_text="As often as you like during your turn (before your attack), you may move 1 damage counter from 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            condition=_can_move,
            effect=_move_counters,
        ),
        Attack(
            title="Psywave",
            game_text="Does 10 more damage for each Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)