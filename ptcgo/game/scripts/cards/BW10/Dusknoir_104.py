from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import move_counters_ability
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack


_move_counters, _can_move = move_counters_ability(1, "theirs")

card = PokemonCardDef(
    guid="d37bb8ee-217f-513d-a591-8e6e477f75b9",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusknoir.Name",
    display_name="Dusknoir",
    searchable_by=["Dusknoir", "Stage 2", "Dusknoir"],
    subtypes=["Stage 2"],
    collector_number=104,
    set_code="BW10",
    rarity=Rarities.RareSecret,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name",
    family_id=477,
    abilities=[
        Ability(
            title="Sinister Hand",
            game_text="As often as you like during your turn (before your attack), you may move 1 damage counter from 1 of your opponent's Pok\u00e9mon to another of your opponent's Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            condition=_can_move,
            effect=_move_counters,
        ),
        Attack(
            title="Shadow Punch",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=ignore_modifier_attack(ignore_resistance=True),
        ),
    ],
)