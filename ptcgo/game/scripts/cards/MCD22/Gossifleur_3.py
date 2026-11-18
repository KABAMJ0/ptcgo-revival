from ptcgo.game.card_effects.support_common import heal_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4997d17d-9110-5bda-9758-2b4bb7bcf3e1",
    key="MCD22",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gossifleur.Name",
    display_name="Gossifleur",
    searchable_by=["Gossifleur", "Basic", "Gossifleur"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="MCD22",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=829,
    abilities=[
        Attack(
            title="Blot",
            game_text="Heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=heal_attack(10),
        ),
    ],
)