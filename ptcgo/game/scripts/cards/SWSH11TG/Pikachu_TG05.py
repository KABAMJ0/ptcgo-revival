from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fa6d6077-5261-5d4a-ae03-7096759813c9",
    key="SWSH11TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="SWSH11TG",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Ability(
            title="Pika Dash",
            game_text="If this Pok\u00e9mon has any Energy attached, it has no Retreat Cost.",
            effect=unimplemented,
        ),
        Attack(
            title="Whimsy Tackle",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)