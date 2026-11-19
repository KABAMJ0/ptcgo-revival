from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="068bbc61-2eb7-50f8-914e-90ca490ef74b",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name",
    display_name="Slakoth",
    searchable_by=["Slakoth", "Basic", "Slakoth"],
    subtypes=["Basic"],
    collector_number=113,
    set_code="SM7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=287,
    abilities=[
        Attack(
            title="Claw",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=flip_or_nothing(),
        ),
        Attack(
            title="Slack Off",
            game_text="Heal all damage from this Pok\u00e9mon. It can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)