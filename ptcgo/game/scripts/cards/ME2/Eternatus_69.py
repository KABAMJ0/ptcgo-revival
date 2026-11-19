from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_stadium_attack, flip_self_lock

card = PokemonCardDef(
    guid="8b936d58-6b48-59fd-8cfb-6e58d2b46ae0",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eternatus.Name",
    display_name="Eternatus",
    searchable_by=["Eternatus", "Basic", "Eternatus"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="ME2",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=890,
    abilities=[
        Attack(
            title="Shatter",
            game_text="Discard a Stadium in play.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=50,
            effect=discard_stadium_attack(),
        ),
        Attack(
            title="Power Rush",
            game_text="Flip a coin. If tails, during your next turn, this Pok\u00e9mon can't use attacks.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=130,
            effect=flip_self_lock(),
        ),
    ],
)