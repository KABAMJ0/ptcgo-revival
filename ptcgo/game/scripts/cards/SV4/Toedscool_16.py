from ptcgo.game.card_effects.support_common import heal_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a77451ba-618e-5434-ae36-86fe81ff148e",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name",
    display_name="Toedscool",
    searchable_by=["Toedscool", "Basic", "Toedscool"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=948,
    abilities=[
        Attack(
            title="Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Absorb",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=heal_attack(20),
        ),
    ],
)