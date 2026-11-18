from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import takes_less_passive

card = PokemonCardDef(
    guid="6aa717ce-df61-51c0-8740-90c3eaca7f19",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blastoiseex.Name",
    display_name="Blastoise ex",
    searchable_by=["Blastoise ex", "Stage 2", "ex", "Blastoiseex"],
    subtypes=["Stage 2", "ex"],
    collector_number=184,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=7,
    abilities=[
        Ability(
            title="Solid Shell",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(30),
        ),
        Attack(
            title="Twin Cannons",
            game_text="Discard up to 2 Basic Water Energy cards from your hand. This attack does 140 damage for each card you discarded in this way.",
            cost={PokemonTypes.WATER: 2},
            damage=140,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)