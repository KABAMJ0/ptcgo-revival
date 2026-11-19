from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.session.effects import is_evolution_pokemon
from ptcgo.game.card_effects.attacks_common import flip_choice


card = PokemonCardDef(
    guid="333783cb-6fce-5b17-a43c-c3689f36aa6a",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkDragonair.Name",
    display_name="Dark Dragonair",
    searchable_by=["Dark Dragonair", "Stage 1", "DarkDragonair"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="BASE6",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    family_id=147,
    abilities=[
        Ability(
            title="Evolutionary Light",
            game_text="Once during your turn (before your attack), you may search your deck for an Evolution card. Show it to your opponent and put it into your hand. Shuffle your deck afterward. This power can't be used if Dark Dragonair is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=lambda board, player_id, pokemon: not pokemon.get_attribute(
                AttrID.SPECIAL_CONDITIONS),
            effect=search_to_hand(is_evolution_pokemon, count=1, reveal=True),
        ),
        Attack(
            title="Tail Strike",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 20 more damage; if tails, this attack does 20 damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            effect=flip_choice(heads=40, tails=20),
        ),
    ],
)