from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.card_effects.support_common import gust_attack

card = PokemonCardDef(
    guid="237e9d02-3d28-5037-b2d1-b51e9c7d25f8",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name",
    display_name="Bellsprout",
    searchable_by=["Bellsprout", "Basic", "Bellsprout"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="HGSS4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=69,
    abilities=[
        Attack(
            title="Inviting Scent",
            game_text="Switch the Defending Pok\u00e9mon with 1 of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gust_attack(damage_to_new_active=0),
        ),
        Attack(
            title="Careless Tackle",
            game_text="Bellsprout does 10 damage to itself.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=recoil_attack(10, damage=0),
        ),
    ],
)