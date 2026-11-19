from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.patterns import is_pokemon_of_type
from ptcgo.game.session.effects import is_evolution_pokemon
from ptcgo.game.card_effects.trainers import all_of
from ptcgo.game.card_effects.passives_common import protect_next_turn


card = PokemonCardDef(
    guid="ae7d4258-21c5-57bc-bfee-899efb4f7e54",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Genesectex.Name",
    display_name="Genesect ex",
    searchable_by=["Genesect ex", "Basic", "ex", "Genesectex"],
    subtypes=["Basic", "ex"],
    collector_number=161,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=649,
    abilities=[
        Ability(
            title="Metallic Signal",
            game_text="Once during your turn, you may search your deck for up to 2 Evolution Metal Pok\u00e9mon, reveal them, and put them into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=search_to_hand(
                all_of(is_evolution_pokemon, lambda card: is_pokemon_of_type(card, "metal")),
                count=2,
                reveal=True,
            ),
        ),
        Attack(
            title="Protect Charge",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=protect_next_turn(reduce=30),
        ),
    ],
)