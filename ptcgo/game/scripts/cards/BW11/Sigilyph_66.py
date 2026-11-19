from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per

card = PokemonCardDef(
    guid="187c42c6-8239-550b-8a68-99a9d6d18cd0",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sigilyph.Name",
    display_name="Sigilyph",
    searchable_by=["Sigilyph", "Basic", "Sigilyph"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="BW11",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=561,
    abilities=[
        Ability(
            title="Safeguard",
            game_text="Prevent all effects of attacks, including damage, done to this Pok\u00e9mon by Pok\u00e9mon-EX.",
            effect=unimplemented,
        ),
        Attack(
            title="Psychic",
            game_text="Does 10 more damage for each Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 10, base=50),
        ),
    ],
)