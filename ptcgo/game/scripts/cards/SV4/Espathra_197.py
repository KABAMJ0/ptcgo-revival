from ptcgo.game.card_effects.passives_common import shield_source_next_turn
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.card_effects.attacks_common import bonus_if, count_discard
from ptcgo.game.card_effects.trainers import named_exactly
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

_tulip_in_discard = lambda ctx: count_discard("mine", named_exactly("Tulip"))(ctx) > 0


card = PokemonCardDef(
    guid="3ee7823d-1d1e-5c88-88b2-71cd8fea2eb6",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espathra.Name",
    display_name="Espathra",
    searchable_by=["Espathra", "Stage 1", "Espathra"],
    subtypes=["Stage 1"],
    collector_number=197,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name",
    family_id=955,
    abilities=[
        Ability(
            title="Stance",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may prevent all damage from and effects of attacks from your opponent's Pok\u00e9mon done to this Pok\u00e9mon until the end of your opponent's next turn.",
            trigger=Triggers.ON_EVOLVE,
            effect=shield_source_next_turn(prevent=True, effects_too=True),
        ),
        Attack(
            title="Glittering Eyes",
            game_text="If Tulip is in your discard pile, this attack does 70 more damage.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=70,
            damage_operator="+",
            effect=bonus_if(_tulip_in_discard, 70),
        ),
    ],
)