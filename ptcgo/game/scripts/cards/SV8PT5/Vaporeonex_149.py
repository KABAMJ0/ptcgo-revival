from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="904170f5-9951-56f7-a77f-4783dfa219f4",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeonex.Name",
    display_name="Vaporeon ex",
    searchable_by=["Vaporeon ex", "Stage 1", "Tera", "ex", "Vaporeonex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=149,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Severe Squall",
            game_text="This attack does 60 damage to each of your opponent's Pok\u00e9mon ex. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Aquamarine",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=280,
            effect=unimplemented,
        ),
    ],
)