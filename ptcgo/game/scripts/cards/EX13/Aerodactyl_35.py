from ptcgo.game.card_effects.passives_common import protect_next_turn
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = PokemonCardDef(
    guid="cb1ec959-e0ec-5b10-855b-428fb092db92",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aerodactyl.Name",
    display_name="Aerodactyl δ",
    searchable_by=["Aerodactyl \u03b4", "Stage 1", "Aerodactyl"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="EX13",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name",
    family_id=142,
    abilities=[
        Ability(
            title="Primal Light",
            game_text="Once during your turn (before your attack), you may search your deck for a basic Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward. This power can't be used if Aerodactyl is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=lambda board, player_id, pokemon: not pokemon.get_attribute(
                AttrID.SPECIAL_CONDITIONS),
            effect=search_to_hand(is_basic_energy_card, count=1, reveal=True),
        ),
        Attack(
            title="Granite Head",
            game_text="During your opponent's next turn, any damage done to Aerodactyl by attacks is reduced by 10 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=protect_next_turn(reduce=10),
        ),
    ],
)