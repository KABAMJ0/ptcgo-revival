from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import flip_protection

card = PokemonCardDef(
    guid="8eda2fa7-cd83-5f1b-a6be-3cb69abc838d",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    display_name="Marill",
    searchable_by=["Marill", "Basic", "Marill"],
    subtypes=["Basic"],
    collector_number=232,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=183,
    abilities=[
        Attack(
            title="Hide",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Flop",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)