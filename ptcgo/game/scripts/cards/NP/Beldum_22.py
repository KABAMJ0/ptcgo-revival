from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.attacks_common import flip_or_nothing, recoil_attack
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.card_effects.patterns import is_pokemon_of_type
from ptcgo.game.card_effects.trainers import all_of

card = PokemonCardDef(
    guid="18cea822-34e6-5dcd-a4cc-8a3d1f7781e2",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    display_name="Beldum",
    searchable_by=["Beldum", "Basic", "Beldum"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=374,
    abilities=[
        Ability(
            title="Magnetic Call",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, search your deck for a Metal Basic Pok\u00e9mon and put it onto your Bench. Shuffle your deck afterward. This power can't be used if Beldum is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            effect=flip_or_nothing(then=search_to_bench(all_of(is_basic_pokemon, lambda card: is_pokemon_of_type(card, "metal")), count=1)),
        ),
        Attack(
            title="Metal Charge",
            game_text="Put 1 damage counter on Beldum.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=recoil_attack(10),
        ),
    ],
)