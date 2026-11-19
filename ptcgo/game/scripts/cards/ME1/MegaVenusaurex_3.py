from ptcgo.game.card_effects.support_common import heal_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="bfc39012-7762-514d-808d-ed256ec36e41",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaVenusaurex.Name",
    display_name="Mega Venusaur ex",
    searchable_by=["Mega Venusaur ex", "Stage 2", "MEGA", "ex", "MegaVenusaurex"],
    subtypes=["Stage 2", "MEGA", "ex"],
    collector_number=3,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=380,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    family_id=1,
    abilities=[
        Ability(
            title="Solar Transfer",
            game_text="As often as you like during your turn, you may use this Ability. Move a Basic Grass Energy from 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Jungle Dump",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 4},
            damage=240,
            effect=heal_attack(30),
        ),
    ],
)