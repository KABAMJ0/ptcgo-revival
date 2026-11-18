from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import protect_next_turn

card = PokemonCardDef(
    guid="fdabdc2a-7f36-51e8-b8de-4e1bbdf9effc",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaZygardeex.Name",
    display_name="Mega Zygarde ex",
    searchable_by=["Mega Zygarde ex", "Basic", "MEGA", "ex", "MegaZygardeex"],
    subtypes=["Basic", "MEGA", "ex"],
    collector_number=124,
    set_code="ME3",
    rarity=Rarities.Rare,
    hp=310,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=718,
    abilities=[
        Attack(
            title="Gaia Wave",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 3},
            damage=200,
            effect=protect_next_turn(reduce=30),
        ),
        Attack(
            title="Nullifying Zero",
            game_text="For each of your opponent's Pok\u00e9mon, flip a coin. If heads, this attack does 150 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 5},
            effect=unimplemented,
        ),
    ],
)