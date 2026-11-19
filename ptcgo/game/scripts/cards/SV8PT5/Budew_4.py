from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_opponent_plays

card = PokemonCardDef(
    guid="b8279d56-193e-5747-b1e1-518fd348ad5e",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Budew.Name",
    display_name="Budew",
    searchable_by=["Budew", "Basic", "Budew"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="SV8PT5",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    family_id=406,
    abilities=[
        Attack(
            title="Itchy Pollen",
            game_text="During your opponent's next turn, they can't play any Item cards from their hand.",
            cost={},
            damage=10,
            effect=lock_opponent_plays("item", damage=10),
        ),
    ],
)