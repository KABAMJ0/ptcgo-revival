from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities
from ptcgo.game.card_effects.attacks_common import lock_opponent_plays

card = PokemonCardDef(
    guid="02fb3e73-87bc-515b-bdc1-43086b22e1b1",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Budew.Name",
    display_name="Budew",
    searchable_by=["Budew", "Basic", "Budew"],
    subtypes=["Basic"],
    collector_number=221,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
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