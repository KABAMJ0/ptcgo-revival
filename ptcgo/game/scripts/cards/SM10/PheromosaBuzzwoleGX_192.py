from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="24e0d674-9379-5ea1-adbb-c1dcfd5b3841",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PheromosaBuzzwoleGX.Name",
    display_name="Pheromosa & Buzzwole-GX",
    searchable_by=["Pheromosa & Buzzwole-GX", "Basic", "TAG TEAM", "GX", "Ultra Beast", "PheromosaBuzzwoleGX"],
    subtypes=["Basic", "TAG TEAM", "GX", "Ultra Beast"],
    collector_number=192,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    hp=260,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=794,
    abilities=[
        Attack(
            title="Jet Punch",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=snipe_attack(30, pool="bench", count=1, apply_modifiers=False),
        ),
        Attack(
            title="Elegant Sole",
            game_text="During your next turn, this Pok\u00e9mon's Elegant Sole attack's base damage is 60.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=unimplemented,
        ),
        Attack(
            title="Beast Game-GX",
            game_text="If your opponent's Pok\u00e9mon is Knocked Out by damage from this attack, take 1 more Prize card. If this Pok\u00e9mon has at least 7 extra Energy attached to it (in addition to this attack's cost), take 3 more Prize cards instead. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)