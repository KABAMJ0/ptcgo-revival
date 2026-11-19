from ptcgo.game.card_effects.attacks_common import reduce_defender_attacks
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="62ceab99-eff4-5b71-b1fe-b6e45553fd0b",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sylveonex.Name",
    display_name="Sylveon ex",
    searchable_by=["Sylveon ex", "Stage 1", "Tera", "ex", "Sylveonex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=86,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Magical Charm",
            game_text="During your opponent's next turn, attacks used by the Defending Pok\u00e9mon do 100 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=reduce_defender_attacks(100),
        ),
        Attack(
            title="Angelite",
            game_text="Choose 2 of your opponent's Benched Pok\u00e9mon. Shuffle those Pok\u00e9mon and all attached cards into your opponent's deck. If 1 of your Pok\u00e9mon used Angelite during your last turn, this attack can't be used.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)